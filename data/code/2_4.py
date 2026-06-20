def parse_volumes(volume_string):
    parts = volume_string.split(',')
    results = []
    errors = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            try:
                results.append(float(stripped))
            except ValueError:
                errors.append(stripped)
    if errors:
        raise ValueError("Non-numeric values found: " + str(errors))
    return results

if __name__ == '__main__':
    sample_input = "1.5, 2.3, 4.7, 0.1"
    print(parse_volumes(sample_input))