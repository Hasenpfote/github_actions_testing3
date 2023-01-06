from pyenv_poetry_tox_pytest_example import utils


def test_add():
    assert utils.add(1, 2) == 3


def test_sub():
    assert utils.sub(4, 3) == 1


def test_mul():
    assert utils.mul(2, 3) == 6


def test_div():
    assert utils.div(4, 2) == 2


def test_muladd():
    assert utils.muladd(2, 3, 4) == 10


def test_print_greet(capfd):
    utils.print_greet()

    out, err = capfd.readouterr()
    assert out == 'Hello, world!\n'
    assert err == ''


def test_print_python_version(capfd):
    utils.print_python_version()

    out, err = capfd.readouterr()
    assert out != ''
    assert err == ''


def test_print_with_delay(capfd, mocker):
    m = mocker.patch(
        'pyenv_poetry_tox_pytest_example.utils.time.sleep', return_value=None
    )

    text = 'Hello, world!'
    utils.print_with_delay(text)

    m.assert_called_once_with(len(text) / 100 + 1.0)
    out, err = capfd.readouterr()
    assert out == text + '\n'
    assert err == ''
