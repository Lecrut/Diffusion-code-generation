import time
from typing import List, Dict, Any
from dataclasses import dataclass
@dataclass
class DataRecord:
    id: int
    value: float
    timestamp: str
def validate_record(record: DataRecord) -> bool:
    if not isinstance(record.id, int):
        raise TypeError("ID must be an integer")
    if record.value < 0 or record.value > 1e6:
        raise ValueError(f"Value {record.value} is out of valid range [0, 1e6]")
    try:
        datetime.fromisoformat(record.timestamp)
    except ValueError:
        raise TypeError("Timestamp must be a valid ISO format string")
    return True
def process_dataset(records: List[DataRecord]) -> Dict[str, Any]:
    if not records:
        return {"status": "empty", "count": 0}
    validated_records = []
    start_time = time.perf_counter()
    for record in records:
        try:
            validate_record(record)
            processed_data = {
                "id": record.id,
                "value_rounded": round(record.value * 1.5),
                "timestamp_normalized": int(time.mktime(datetime.strptime(record.timestamp, "%Y-%m-%dT%H:%M:%S").timetuple()))
            }
            validated_records.append(processed_data)
        except Exception as e:
            print(f"Error processing record {record.id}: {e}")
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return {
        "status": "success",
        "total_records": len(records),
        "processed_count": len(validated_records),
        "execution_time_ms": round(execution_time_ms, 2),
        "sample_output": validated_records[:3] if len(validated_records) > 0 else []
    }
if __name__ == '__main__':
    sample_data = [
        DataRecord(id=1, value=54.32, timestamp="2023-10-05T14:30:00"),
        DataRecord(id=2, value=-98.76, timestamp="invalid-date"),
        DataRecord(id=3, value=1e6 + 10, timestamp="2023-10-06T09:15:45"),
        DataRecord(id=4, value=12.5, timestamp="2023-10-07T18:20:10")
    ]
    result = process_dataset(sample_data)
    print(f"Processing Result: {result}")