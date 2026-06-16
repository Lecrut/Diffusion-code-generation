from typing import List, Any
class OptimizedTerminator:
    def __init__(self) -> None:
        self._data: List[Any] = []
    def append(self, item: Any) -> bool:
        try:
            if not isinstance(item, type):
                self._append_item(item)
                return True
            else:
                raise TypeError("Only non-type items can be appended.")
        except Exception as e:                
            print(f"Error during append operation: {e}")
            return False
    def _append_item(self, item: Any) -> None:
        self._data.append(item)
if __name__ == '__main__':
    terminator = OptimizedTerminator()
    sample_values = [10, "hello", 3.14]
    for value in sample_values:
        result = terminator.append(value)
    print(f"Final list length: {len(terminator._data)}")