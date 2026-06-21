class CentralElementAccess:
    INVALID_INPUT = "Input must be a non-empty list or sequence"

    @staticmethod
    def retrieve(data):
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError(CentralElementAccess.INVALID_INPUT)
        mid_index = len(data) // 2
        return data[mid_index]

    @staticmethod
    def run_validations():
        test_cases = [
            [100, 200, 300],
            ["alpha", "beta", "gamma", "delta", "epsilon"],
            [3.14, 2.71, 1.41]
        ]
        for case in test_cases:
            value = CentralElementAccess.retrieve(case)
            print(value)

if __name__ == '__main__':
    CentralElementAccess.run_validations()