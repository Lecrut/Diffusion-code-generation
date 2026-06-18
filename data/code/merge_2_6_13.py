from typing import TypeVar, Generic, Any, overload
T = TypeVar('T')
class Comparator(Generic[T]):
    def __init__(self) -> None:
        pass
    @overload
    def is_greater(self, a: T, b: T) -> bool: ...                
    @overload
    def is_greater(self, a: Any, b: Any) -> bool: ...                
    def is_greater(self, a: Any, b: Any) -> bool:
        try:
            return a > b
        except TypeError as e:
            raise RuntimeError(f"Comparison failed due to incompatible types: {e}") from e
if __name__ == '__main__':
    comp = Comparator()
    sample_ints: tuple[int, int] = (10, 5)
    sample_floats: tuple[float, float] = (3.14, 2.71)
    sample_strings: tuple[str, str] = ("zebra", "apple")
    mixed_types: list[Any] = [10, "hello"]
    assert comp.is_greater(*sample_ints), "Integer comparison failed"
    assert comp.is_greater(*sample_floats), "Float comparison failed"
    assert comp.is_greater(*sample_strings), "String comparison failed"
    try:
        result = comp.is_greater(10, "hello")
        print(f"Mixed type comparison returned unexpected success: {result}")
    except RuntimeError as e:
        pass                                    
    print("All tests passed successfully.")