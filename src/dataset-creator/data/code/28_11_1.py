from collections import OrderedDict
class AnimalValidator:
    ALLOWED_ANIMALS = {"lion", "tiger", "elephant"}
    @classmethod
    def is_valid_animal(cls, entry):
        return entry.lower().strip() in cls.ALLOWED_ANIMALS
class AnimalListProcessor(OrderedDict):
    def __init__(self):
        super().__init__()
        self.validator = AnimalValidator()
    def add_entry(self, entry: str) -> bool:
        normalized = entry.lower().strip()
        if not self.validator.is_valid_animal(normalized):
            return False
        if normalized in self:
            return False
        self[normalized] = True
        return True
def process_animals(raw_list) -> list[str]:
    processor = AnimalListProcessor()
    result_keys = []
    for item in raw_list:
        if isinstance(item, str) and not (item == "" or " " in item):
            success = processor.add_entry(item)
            if success:
                normalized_key = list(processor.keys())[-1]
                result_keys.append(normalized_key)
    return result_keys
if __name__ == '__main__':
    sample_data = [
        "Lion", 
        "Tiger", 
        "", 
        "  elephant  ", 
        "lion", 
        "dog", 
        "tiger"
    ]
    final_list = process_animals(sample_data)
    print(final_list)