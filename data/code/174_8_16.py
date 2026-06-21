def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == '__main__':
    data = {
        "library": {
            "books": {
                "fiction": ["To Kill a Mockingbird", "1984"],
                "non-fiction": {"history": "A Brief History of Time"}
            },
            "magazines": ["Time", "National Geographic"]
        }
    }

    flattened_data = flatten_dict(data)
    print(flattened_data)