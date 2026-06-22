def nanometers_to_meters(nanometers):
    if not isinstance(nanometers, (int, float)):
        raise ValueError("Input must be a number.")
    return nanometers * 1e-9

if __name__ == '__main__':
    sample_nanometers = 1000000
    meters = nanometers_to_meters(sample_nanometers)
    print(f"{sample_nanometers} nanometers is equal to {meters} meters")