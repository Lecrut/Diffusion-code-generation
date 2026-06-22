import csv
import io

def calculate_average_temperature(file_content: str) -> float:
    if not file_content.strip():
        raise ValueError("File content is empty")

    reader = csv.DictReader(io.StringIO(file_content))
    temperatures = []
    
    for row in reader:
        try:
            temp_str = row.get('temperature')
            if temp_str is None:
                raise KeyError("temperature")
            temp = float(temp_str)
            temperatures.append(temp)
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid temperature data: {e}")
            
    if not temperatures:
        raise ValueError("No valid temperature readings found")
        
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_csv = """date,temperature
2023-01-01,20.5
2023-01-02,22.0
2023-01-03,19.5"""

    result = calculate_average_temperature(sample_csv)
    print(result)