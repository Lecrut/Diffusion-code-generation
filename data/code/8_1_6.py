def _is_meaningful(segment: str) -> bool:
    stripped = segment.strip()
    return len(stripped) > 0

def _split_and_filter(raw_text: str) -> list[str]:
    if not raw_text:
        return []
    raw_parts = raw_text.split(',')
    return [part for part in raw_parts if _is_meaningful(part)]

class CsvProcessor:
    def __init__(self, text: str):
        self.text = text
    
    def get_meaningful_segments(self) -> list[str]:
        return _split_and_filter(self.text)

if __name__ == '__main__':
    sample_input = "alpha,,beta,  ,gamma,,,delta, epsilon "
    processor = CsvProcessor(sample_input)
    output = processor.get_meaningful_segments()
    print(output)