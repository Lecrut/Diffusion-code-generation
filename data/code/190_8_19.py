SUBSTRING_TO_SEARCH = "example"
DATA_LISTS = [
    ["apple", "banana", "cherry"],
    ["python", "java", "c++", "ruby"],
    ["dog", "cat", "bird"]
]

def substring_exists_in_list(data_lists, search_term):
    return any(search_term in sublist for sublist in data_lists)

if __name__ == '__main__':
    results = [substring_exists_in_list(lists, SUBSTRING_TO_SEARCH) for lists in DATA_LISTS]
    print(results)