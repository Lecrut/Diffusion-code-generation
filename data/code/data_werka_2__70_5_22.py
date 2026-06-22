class EndPointValidator:
    def __init__(self, sequence):
        self.sequence = sequence
        self._status_map = {
            0: "empty",
            1: "singleton",
            2: "valid_pair",
            3: "valid_multi"
        }

    def _get_status(self):
        length = len(self.sequence)
        if length == 0:
            return self._status_map[0]
        if length == 1:
            return self._status_map[1]
        if length == 2:
            return self._status_map[2]
        return self._status_map[3]

    def validate_and_return_ends(self):
        status = self._get_status()
        if status in (self._status_map[0], self._status_map[1]):
            raise ValueError(f"Sequence has {len(self.sequence)} elements, requires at least 2")
        
        first_element = self.sequence[0]
        last_element = self.sequence[-1]
        
        if first_element == last_element and status == self._status_map[2]:
            return (first_element, last_element, "duplicate_bounds")
        
        return (first_element, last_element, status)

if __name__ == '__main__':
    data_set = [10, 20, 30, 40, 50]
    validator = EndPointValidator(data_set)
    result = validator.validate_and_return_ends()
    print(result)