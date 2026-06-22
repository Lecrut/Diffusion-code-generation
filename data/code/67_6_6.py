LITER_SCALE = 1000

def liters_to_milliliters(volume: float) -> float:
    if volume < 0:
        raise ValueError("Volume cannot be negative")
    return volume * LITER_SCALE

if __name__ == '__main__':
    sample_value = 2.5
    print(liters_to_milliliters(sample_value))