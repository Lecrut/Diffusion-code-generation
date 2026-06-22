import math

KILOMETERS_TO_METERS = 1000.0
METERS_TO_FEET = 3.28084

def convert_lengths(kilometers_list):
    results = []
    for km in kilometers_list:
        meters = km * KILOMETERS_TO_METERS
        feet = meters * METERS_TO_FEET
        results.append((km, meters, feet))
    return results

def format_output(results):
    lines = []
    for km, meters, feet in results:
        lines.append(f"{km} km = {meters} m = {feet} ft")
    return "\n".join(lines)

if __name__ == '__main__':
    sample_kilometers = [1.0, 5.5, 12.34, 100.0, 0.25]
    converted = convert_lengths(sample_kilometers)
    output = format_output(converted)
    print(output)