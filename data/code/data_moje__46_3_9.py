def max_salary(records):
    return max(map(lambda r: float(r["salary"]) if isinstance(r, dict) and "salary" in r and isinstance(r["salary"], (int, float)) else 0.0, records))

if __name__ == '__main__':
    sample_records = [
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": 85000},
        {"name": "Charlie", "salary": 92000},
        {"name": "Diana", "salary": "invalid"},
        {"name": "Eve", "salary": 78000}
    ]
    print(max_salary(sample_records))