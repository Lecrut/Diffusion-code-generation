import numpy as np

class BooleanOrchestrator:
    TRUE_VALUE = 1
    FALSE_VALUE = 0

    def __init__(self, data):
        self._data = data

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, (list, tuple, np.ndarray)):
            raise ValueError("Input must be a list, tuple, or numpy array")
        if len(data) == 0:
            raise ValueError("Input cannot be empty")
        return data

    def check_any_true(self):
        data = self._validate_input(self._data)
        if isinstance(data, np.ndarray):
            return bool(np.any(data))
        return any(data)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    sample_array = np.array([False, False, False, False])
    sample_array_true = np.array([False, True, False, False])
    
    checker_list = BooleanOrchestrator(sample_list)
    result_list = checker_list.check_any_true()
    
    checker_array = BooleanOrchestrator(sample_array)
    result_array = checker_array.check_any_true()
    
    checker_array_true = BooleanOrchestrator(sample_array_true)
    result_array_true = checker_array_true.check_any_true()
    
    print(result_list)
    print(result_array)
    print(result_array_true)