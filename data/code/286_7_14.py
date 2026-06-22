PM_TO_M = 1e-12

def pm_to_meters(pm_value):
    return pm_value * PM_TO_M

if __name__ == '__main__':
    sample_values = [10**6, 5.34e-18, 789e9]
    for val in sample_values:
        print(f"{val} picometers is {pm_to_meters(val)} meters")