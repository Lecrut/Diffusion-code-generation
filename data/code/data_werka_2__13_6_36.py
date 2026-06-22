class TimeZoneManager:
    MIN_OFFSET = float('inf')
    MAX_OFFSET = float('-inf')

    def __init__(self, offsets):
        if not offsets:
            raise ValueError("The list of time zone offsets cannot be empty.")
        self.offsets = offsets
        self._update_min_max_offsets()

    def _update_min_max_offsets(self):
        TimeZoneManager.MIN_OFFSET = min(self.offsets)
        TimeZoneManager.MAX_OFFSET = max(self.offsets)

    @staticmethod
    def calculate_difference():
        return TimeZoneManager.MAX_OFFSET - TimeZoneManager.MIN_OFFSET

if __name__ == '__main__':
    sample_offsets = [-5, 10, 3.2, -7, 6]
    manager = TimeZoneManager(sample_offsets)
    difference = TimeZoneManager.calculate_difference()
    print(difference)