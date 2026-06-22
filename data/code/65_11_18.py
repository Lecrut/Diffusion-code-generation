def feet_to_inches(feet_list):
    return [f * 12 for f in feet_list]

if __name__ == '__main__':
    samples = [1.5, 3, 6.25, 0]
    result = feet_to_inches(samples)
    print(result)