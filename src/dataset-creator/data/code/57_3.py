from typing import List, Any, Optional
class DataModule:
    def get(self, data: List[Any], index: int, default: Any = None) -> Any:
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        try:
            return data[index]
        except IndexError:
            pass
        return default
    def set(self, data: List[Any], index: int, value: Any) -> None:
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        valid_index = False
        try:
            _ = data[index]
            valid_index = True
        except IndexError:
            pass
        if valid_index and 0 <= index < len(data):
            data[index] = value
    def validate(self, data: List[Any]) -> bool:
        return isinstance(data, list)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    module = DataModule()
    if not module.validate(sample_data):
        print("Dataset integrity failed.")
    else:
        retrieved_value = module.get(sample_data, -5)
        updated_sample = sample_data.copy()
        module.set(updated_sample, 2, "updated")
        result_list = [module.get(updated_sample, i) for i in range(len(updated_sample))]
    print(result_list)