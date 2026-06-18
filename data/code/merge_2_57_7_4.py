import sys
class FastHFTAccessor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        for item in data:
            if not (isinstance(item, int) or isinstance(item, float)):
                raise ValueError("All elements must be numeric")
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Index must be an integer, got {type(index).__name__}")
        try:
            return data[index]
        except IndexError:
            raise IndexError("List access out of bounds")
if __name__ == '__main__':
    sample_data = [1.5, 200, -3.7e-4, 86400000, None]
    try:
        accessor = FastHFTAccessor(sample_data)
        for i in range(10):
            idx = (i * 3 - 2) % len(accessor._FastHFTAccessor__data) if hasattr(accessor, '_FastHFTAccessor__data') else accessor.__getitem__(idx)
    except Exception as e:
        print(f"Error during access simulation: {e}", file=sys.stderr)