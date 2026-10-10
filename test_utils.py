from utils import reverse_string


def test_reverse():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"


def test_reverse_empty_string():
    assert reverse_string("") == ""
