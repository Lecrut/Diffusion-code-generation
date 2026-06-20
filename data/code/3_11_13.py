import argparse
import csv
import sys
from pathlib import Path

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Convert temperature data from Celsius to Fahrenheit.')
    parser.add_argument(
        'input_file',
        type=Path,
        help='Path to the input CSV file containing Celsius temperatures.'
    )
    parser.add_argument(
        'output_file',
        type=Path,
        nargs='?',
        default=None,
        help='Path to the output CSV file. If omitted, prints to stdout.'
    )
    parser.add_argument(
        '--delimiter',
        type=str,
        default=',',
        help='Delimiter used in the input CSV file. Default is comma.'
    )
    parser.add_argument(
        '--temperature-column',
        type=int,
        default=0,
        help='Index of the column containing temperature values. Default is 0.'
    )
    return parser.parse_args(argv)

def process_file(input_path: Path, output_path: Path | None, delimiter: str, temp_col_idx: int) -> str:
    if not input_path.exists():
        raise FileNotFoundError(f'Input file not found: {input_path}')
    
    if not input_path.is_file():
        raise IsADirectoryError(f'Input path is a directory, not a file: {input_path}')

    results = []
    
    try:
        with input_path.open('r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=delimiter)
            
            for row_idx, row in enumerate(reader):
                if row_idx == 0:
                    results.append(row)
                    continue
                
                if temp_col_idx < 0 or temp_col_idx >= len(row):
                    raise ValueError(f'Row {row_idx}: Column index {temp_col_idx} is out of range for row with length {len(row)}')
                
                try:
                    temp_value = float(row[temp_col_idx])
                except ValueError:
                    raise ValueError(f'Row {row_idx}: Cannot convert value "{row[temp_col_idx]}" to float')
                
                converted_temp = celsius_to_fahrenheit(temp_value)
                
                new_row = list(row)
                new_row[temp_col_idx] = str(converted_temp)
                results.append(new_row)
                
    except UnicodeDecodeError:
        raise ValueError(f'Input file {input_path} contains non-UTF-8 encoded data.')

    output_string = csv.writer(
        sys.stdout if output_path is None else open(output_path, 'w', newline='', encoding='utf-8')
    ).writerows(results) if output_path is None else csv.writer(
        open(output_path, 'w', newline='', encoding='utf-8')
    ).writerows(results)
    
    if output_path is not None:
        sys.stdout.flush()
        
    return str(input_path)

def main():
    args = parse_arguments([
        'celsius_data.csv',
        'fahrenheit_data.csv',
        '--delimiter', ',',
        '--temperature-column', '1'
    ])

    try:
        result_path = process_file(
            input_path=args.input_file,
            output_path=args.output_file,
            delimiter=args.delimiter,
            temp_col_idx=args.temperature_column
        )
        print(result_path)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()