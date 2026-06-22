from datetime import datetime

def filter_records(records):
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    filtered = []
    for record in records:
        value = record.get("value", 0)
        status = record.get("status", "")
        date_str = record.get("date", "")
        category = record.get("category", "")
        is_verified = record.get("is_verified", False)

        cond1 = value > 10
        cond2 = status == "active"
        cond3 = is_valid_date(date_str)
        cond4 = category in ["A", "B", "C"]
        cond5 = is_verified is True

        if cond1 and cond2 and cond3 and cond4 and cond5:
            filtered.append(record)

    return filtered

if __name__ == "__main__":
    sample_records = [
        {"value": 15, "status": "active", "date": "2023-01-01", "category": "A", "is_verified": True},
        {"value": 5, "status": "active", "date": "2023-01-02", "category": "A", "is_verified": True},
        {"value": 20, "status": "inactive", "date": "2023-01-03", "category": "B", "is_verified": True},
        {"value": 25, "status": "active", "date": "invalid-date", "category": "C", "is_verified": True},
        {"value": 30, "status": "active", "date": "2023-01-05", "category": "D", "is_verified": True},
        {"value": 50, "status": "active", "date": "2023-01-06", "category": "B", "is_verified": False},
        {"value": 12, "status": "active", "date": "2023-01-07", "category": "A", "is_verified": True},
    ]

    result = filter_records(sample_records)
    print(result)