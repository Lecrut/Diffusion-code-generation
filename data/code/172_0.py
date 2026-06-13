if __name__ == '__main__':
    data = {
        "apple": "fruit",
        "zebra": "animal",
        "banana": "fruit",
        "cat": "animal",
        "dog": "animal"
    }
    words = list(data.values())
    words.sort()
    print(words)