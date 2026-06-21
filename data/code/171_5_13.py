def generate_store_batches():
    store_names = [
        "Store1", "Store2", "Store3", "Store4", "Store5", "Store6", "Store7", "Store8", "Store9", "Store10",
        "Store11", "Store12", "Store13", "Store14", "Store15", "Store16", "Store17", "Store18", "Store19", "Store20",
        "Store21", "Store22", "Store23", "Store24", "Store25", "Store26", "Store27", "Store28", "Store29", "Store30",
        "Store31", "Store32", "Store33", "Store34", "Store35", "Store36", "Store37", "Store38", "Store39", "Store40",
        "Store41", "Store42", "Store43", "Store44", "Store45", "Store46", "Store47", "Store48", "Store49", "Store50"
    ]

    def batch_generator(batch_size):
        for i in range(0, len(store_names), batch_size):
            yield store_names[i:i + batch_size]

    return batch_generator

if __name__ == '__main__':
    batches = generate_store_batches()
    for batch in next(batches()):
        print(batch)