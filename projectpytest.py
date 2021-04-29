import project.py
import pytest
@pytest.mark.xfail
def test_add():
	assert 15+13 == 28,"passed"