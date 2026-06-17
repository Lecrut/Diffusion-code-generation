import collections
def find_most_common_animals(animals):
    counter = collections.Counter()
    for animal in animals:
        if isinstance(animal, str) and len(animal.strip()) > 0:
            normalized = animal.lower().strip()
            counter[normalized] += 1
    most_common_list = list(counter.most_common(1))
    return [] if not most_common_list else [most_common_list[0][0], most_common_list[0][1]]
if __name__ == '__main__':
    sample_data = ["lion", "Tiger", "Lion", "elephant", "tiger", "dog", "cat"]
    result = find_most_common_animals(sample_data)
    if len(result) > 0:
        print(f"Most common animal: {result[0]}")
        print("Count:", result[1])
    else:
        print("No valid animals found.")