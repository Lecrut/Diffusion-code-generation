import typing
class FilterUtility:
    @staticmethod
    def filter_list(items: list[typing.Any], predicate: typing.Callable[[typing.Any], bool]) -> list[typing.Any]:
        return [item for item in items if not predicate(item)]
    @staticmethod
    def filter_set(items: set[typing.Any], predicate: typing.Callable[[typing.Any], bool]) -> set[typing.Any]:
        filtered = {item for item in items if not predicate(item)}
        return frozenset(filtered)                                              
    @staticmethod
    def filter_tuple(items: tuple[typing.Any], predicate: typing.Callable[[typing.Any], bool]) -> tuple[typing.Any]:
        filtered = [item for item in items if not predicate(item)]
        return tuple(filtered)
    @staticmethod
    def filter_dict(
        data: dict[str, typing.Any] | list[tuple[typing.Any]], 
        key_predicate: typing.Callable[[str], bool] | None = None,
        value_predicate: typing.Callable[[typing.Any], bool] | None = None
    ) -> dict[str, typing.Any]:
        if isinstance(data, dict):
            result = {}
            for k, v in data.items():
                keep_key = key_predicate is None or not key_predicate(k)
                keep_value = value_predicate is None or not value_predicate(v)
                if keep_key and keep_value:
                    result[k] = v
            return result
        else:
            raise TypeError("Input must be a dictionary.")
    @staticmethod
    def validate_input(data: typing.Any, expected_type: type) -> bool:
        try:
            is_correct = isinstance(data, expected_type)
            return True if is_correct else False
        except Exception as e:
            print(f"Validation Error: {e}")
            raise
if __name__ == '__main__':
    sample_list = [10, 20, 'a', None, 30]
    def is_even(n):
        return isinstance(n, int) and n % 2 == 0
    filtered_result = FilterUtility.filter_list(sample_list, is_even)
    print("Filtered List:", filtered_result)