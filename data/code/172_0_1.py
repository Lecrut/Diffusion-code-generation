if __name__ == '__main__':
    data = {
        "apple": "fruit",
        "zebra": "animal",
        "banana": "fruit",
        "cat": "mammal",
        "dog": "mammal"
    }
    words = list(data.values())
    words.sort()
    print(words)