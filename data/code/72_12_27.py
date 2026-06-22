class AdjacentInequalityFinder:
    STEP_VALUE = 1
    RESULT_KEYS = ('index', 'left', 'right')

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        if len(data) < 2:
            raise ValueError("Input must contain at least two elements")
        return data

    def find(self, data):
        validated_data = self._validate_input(data)
        found_inequalities = []
        limit = len(validated_data) - 1
        idx = 0
        while idx < limit:
            current_val = validated_data[idx]
            next_val = validated_data[idx + 1]
            if current_val != next_val:
                found_inequalities.append({
                    'index': idx,
                    'left': current_val,
                    'right': next_val
                })
            idx += self.STEP_VALUE
        return found_inequalities

if __name__ == '__main__':
    input_sequence = [10, 10, 20, 30, 30, 40, 50, 50, 50, 60]
    finder_instance = AdjacentInequalityFinder()
    results = finder_instance.find(input_sequence)
    print(results)