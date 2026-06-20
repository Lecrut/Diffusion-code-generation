import datetime

def fractional_day_to_seconds(fractional_day):
    if not isinstance(fractional_day, float) or fractional_day < 0 or fractional_day > 1:
        raise ValueError('Fractional day must be a float between 0 and 1')
    return fractional_day * 24 * 3600
if __name__ == '__main__':
    sample_fractional_day = 0.5
    seconds = fractional_day_to_seconds(sample_fractional_day)
    print(seconds)