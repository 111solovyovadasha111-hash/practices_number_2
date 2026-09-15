import pytest
from subpref import fast, brutforce

@pytest.fixture(params=[brutforce, fast])
def choose_func(request):
    return request.param

def test_simple(choose_func):
    length, pair = choose_func(["abc", "cde"])
    assert length == 1
    assert set(pair) == {"abc", "cde"}

def test_no_match(choose_func):
    length, pair = choose_func(["abc", "def"])
    assert length == 0
    assert pair == []

def test_prefix_full_words(choose_func):
    length, pair = choose_func(["ab", "xab"])
    assert length == 2
    assert set(pair) == {"ab", "xab"}

def test_longest_prefix(choose_func):
    length, pair = choose_func(["ab", "abcd", "abc"])
    assert length == 3
    assert set(pair) == {"abcd", "abc"}

def test_one_word(choose_func):
    length, pair = choose_func(["abc"])
    assert length == 0
    assert pair == []

def test_no_words(choose_func):
    length, pair = choose_func([])
    assert length == 0
    assert pair == []

def test_mucho_words(choose_func):
    length, pair = choose_func(["JjA3python",
        "0QfNiFfcop",
        "9ks7XiLEYC",
        "2qWrM78h",
        "zjj511XFd",
        "pythonf"])
    assert length == 6
    assert set(pair) == {"JjA3python", "pythonf"}


@pytest.mark.parametrize("words", [
        ["abc", "cde"],
        ["abc", "xyz"],
        ["ab", "xab"],
        ["abc", "xabc", "xxc"],
        ["abc"],
        [],
        ["abc", "abc"],
        ["hello", "loworld", "worldwide", "widecase"],
        ["aaa", "aaaa", "aaaaa"],
        ["x", "y", "z"],
        ["prefix", "fixture", "iffifi"],
    ])
def test_fast_equals_brutforce(words):
    assert fast(words)[0] == brutforce(words)[0]
    assert set(fast(words)[1]) == set(brutforce(words)[1])

