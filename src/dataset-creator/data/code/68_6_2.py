import re
def convert_volume_strings(volumes: list) -> float:
    def parse_single(value):
        cleaned = value.strip()
        if not cleaned or 'N/A' in cleaned.upper():
            return None
        try:
            val = float(cleaned.replace('L', '').replace('l', ''))
            val = float(re.sub(r'[Ll]', '', cleaned))
            return val
        except ValueError:
            try:
                val = float(cleaned.replace('%', '').replace('ml', 'm').lower())                                                                           
            except ValueError:
                try:
                    val = float(re.sub(r'[Ll]', '', cleaned))
                    if '%' in cleaned and not re.match(r'^-?\d*\.?\d+$', cleaned):
                        return None
                except ValueError:
                    return None
            return val
    parsed = []
    for item in volumes:
        try:
            cleaned_item = re.sub(r'[Ll]', '', str(item))
            if not cleaned_item or 'N/A' in str(cleaned_item).upper():
                continue
            val = float(cleaned_item)
        except ValueError:
            try:
                parts = item.split()
                for part in parts:
                    if re.match(r'^-?\d+\.?\d*$', part):
                        val = float(part.replace('L', '').replace('l', ''))
                        break
            except ValueError:
                continue
        parsed.append(val)
    return sum(parsed) / len(volumes)
if __name__ == '__main__':
    sample_data = ["1.5 L", "2 ml", "N/A", "-3e-4 l", "", "0"]
    result = convert_volume_strings(sample_data)