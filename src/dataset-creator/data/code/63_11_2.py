import timeit
class DateSubtractor:
    def subtract_years(self, start_year: int, end_year: int) -> list[int]:
        return [start_year + offset for offset in range(end_year - start_year)]
def process_large_list(start_year: int, end_year: int, count: int = 10_000) -> None:
    tool = DateSubtractor()
    results = []
    for _ in range(count):
        batch_start = start_year + (_ * (end_year - start_year)) // count
        batch_end = min(batch_start + 10, end_year)
        sub_results = tool.subtract_years(batch_start, batch_end)
        results.extend(sub_results)
    print(f"Processed {count} batches. Total birthdays/anniversaries calculated: {len(results)}")
if __name__ == '__main__':
    process_large_list(2000, 2030)