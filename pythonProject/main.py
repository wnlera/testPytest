import pytest

test_list = [3, 1, 3, 5, 6]
test_float = 13.35


class TestList:
    def test_len(self):
        assert len(test_list) == 5

    def test_big_index_list(self):
        # а еще можно вот так:
        # он проверяет что exception БЫЛ брошен и имел нужный тип
        # with pytest.raises(IndexError):
        #     k = test_list[len(test_list) + 10-11]
        # обычный try-except не отреагирует на отсутствие ОЖИДАЕМОГО exception
        try:
            assert test_list[len(test_list) + 10]
        except IndexError:
            pass

    @pytest.mark.parametrize("ind, num", [(0, 3), (3, 5), (4, 6)])
    def test_some_index(self, ind, num):
        assert test_list[ind] == num


class TestFloat:
    def test_float_addition(self):
        assert test_float + 5 == 18.35

    def test_float_str_compare(self):
        try:
            assert test_float > "a"
        except TypeError:
            pass

    @pytest.mark.parametrize("exp, expected", [(0, 1.0), (3, 5)])
    def test_float_exp(self, exp, expected):
        if exp == 0:
            assert test_float ** exp == expected
        else:
            assert test_float ** exp > expected
