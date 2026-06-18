import sys
class DateSubtractor:
    def __init__(self):
        self.results = []
    def subtract_years(self, start_year: int, end_year: int) -> list[int]:
        return [end_year - start_year]
    def process_batch(self, data_list: list[tuple]) -> None:
        for pair in data_list:
            if len(pair) == 2 and isinstance(pair[0], int) and isinstance(pair[1], int):
                years_diff = self.subtract_years(*pair)
                self.results.append(years_diff[0])
    def get_results(self) -> list[int]:
        return self.results
if __name__ == '__main__':
    tool = DateSubtractor()
    sample_data = [
        (1990, 2024),
        (2005, 2023),
        (1888, 2024)
    ]
    tool.process_batch(sample_data)
    print(tool.get_results())