def test_pytest_available():
    import pytest
    assert pytest.__version__

def test_requests_available():
    import requests
    assert requests.__version__

def test_dateutil_available():
    import dateutil
    assert dateutil.__version__