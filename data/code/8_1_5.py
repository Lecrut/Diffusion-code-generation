import re

def parse_csv_meaningful_segments(csv_string):
    if not csv_string or not isinstance(csv_string, str):
        return []
    segments = csv_string.split(',')
    return [segment.strip() for segment in segments if segment.strip()]

if __name__ == '__main__':
    sample_input = ",apple,,banana,  ,cherry, , date ,,,"
    result = parse_csv_meaningful_segments(sample_input)
    print(result)
    sample_input_2 = "  ,  ,  "
    result_2 = parse_csv_meaningful_segments(sample_input_2)
    print(result_2)
    sample_input_3 = "red,green,blue"
    result_3 = parse_csv_meaningful_segments(sample_input_3)
    print(result_3)
    sample_input_4 = ""
    result_4 = parse_csv_meaningful_segments(sample_input_4)
    print(result_4)