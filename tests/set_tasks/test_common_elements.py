from tasks.set_tasks.common_elements import common_elements


def test_common_elements(new_set):
    result = common_elements(new_set, {2, 5, 7, 20, -13})
    assert result == {2, 5, 7}