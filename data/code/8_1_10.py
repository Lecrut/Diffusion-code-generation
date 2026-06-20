import csv
import io

def split_csv_string(csv_text: str) -> list[str]:
    if not csv_text or not csv_text.strip():
        return []
    reader = csv.reader(io.StringIO(csv_text))
    rows = list(reader)
    meaningful_segments = []
    for row in rows:
        for segment in row:
            if segment.strip():
                meaningful_segments.append(segment)
    return meaningful_segments
if __name__ == '__main__':
    sample_csv = 'apple,,banana,  ,cherry,,,date'
    result = split_csv_string(sample_csv)
    print(result)