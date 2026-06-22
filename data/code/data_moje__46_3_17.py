mixed_records = [
    {"name": "Alice", "salary": 75000},
    {"name": "Bob", "salary": "not_a_number"},
    {"name": "Charlie", "salary": 92000},
    {"name": "Diana", "salary": 68000},
    {"name": "Eve", "salary": 85000}
]
def extract_max_salary(records):
    return max(map(lambda r: r["salary"] if isinstance(r.get("salary"), (int, float)) else 0, records))
if __name__ == '__main__':
    print(extract_max_salary(mixed_records))