import csv
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
class DataProcessor:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist.")
    def load_data(self) -> List[Dict[str, Any]]:
        data: List[Dict[str, Any]] = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cleaned_row: Dict[str, Any] = {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}
                    data.append(cleaned_row)
        except PermissionError as e:
            raise RuntimeError(f"Permission denied to read file: {e}") from e
        return data
    def process_large_dataset(self, batch_size: int = 10_000) -> Dict[str, Any]:
        start_time = datetime.now()
        processed_count = 0
        try:
            if self.file_path.exists():
                raw_data = self.load_data()
                for i in range(0, len(raw_data), batch_size):
                    chunk = raw_data[i:i + batch_size]
                    processed_chunk = []
                    for item in chunk:
                        try:
                            result_item = {**item}
                            if 'value' in result_item and isinstance(result_item['value'], str):
                                numeric_val = float(result_item['value'])
                                result_item['processed_value'] = round(numeric_val * 1.5, 2)
                            processed_chunk.append(result_item)
                        except ValueError:
                            continue
                    time.sleep(0.001) 
                total_time = (datetime.now() - start_time).total_seconds()
                return {
                    'success': True,
                    'rows_processed': len(raw_data),
                    'processing_time_ms': round(total_time * 1000, 2),
                    'batch_size_used': batch_size
                }
        except Exception as e:
            raise RuntimeError(f"Processing failed with error: {e}") from e
if __name__ == '__main__':
    processor = DataProcessor("sample_data.csv")
    try:
        result = processor.process_large_dataset(batch_size=500)
        print(json.dumps(result, indent=2))
    except Exception as error:
        print(f"Error occurred during execution: {error}")