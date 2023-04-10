from utils import arrs


def test_get():
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get('str', 1, 'test') == 'Тип данных не является списком'
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], '2', 'test') == 'Индекс указон не корректно'
    assert arrs.get([1, 2, 3, 4], [1, 2], 'test') == 'Индекс указон не корректно'

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice('asd', 2) == 'Тип данных не является списком'
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]
