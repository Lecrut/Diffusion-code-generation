import statistics

def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    single_element_list = [99]

    means = {
        "sample_list": calculate_mean(sample_list),
        "empty_list": calculate_mean(empty_list),
        "single_element_list": calculate_mean(single_element_list)
    }

    for key, value in means.items():
        print(f"Mean of {key}: {value}")