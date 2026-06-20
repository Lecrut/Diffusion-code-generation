def split_csv_meaningful(text: str) -> list:
    if text == "":
        return []
    
    parts = text.split(",")
    result = []
    
    for part in parts:
        stripped = part.strip()
        if stripped != "":
            result.append(stripped)
            
    return result

if __name__ == '__main__':
    sample_csv = "apple,,banana, ,cherry,date,,fig"
    meaningful_segments = split_csv_meaningful(sample_csv)
    print(meaningful_segments)