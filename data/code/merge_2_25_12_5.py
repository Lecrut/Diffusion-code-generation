import hashlib
class AreaColorMapper:
    def __init__(self):
        self.color_map = {
            "downtown": "#FF5733",
            "suburbs": "#3498DB",
            "industrial": "#2ECC71",
            "residential": "#ECF0F1"
        }
    def generate_color(self, area_string: str) -> str:
        normalized_key = self._normalize_input(area_string.lower())
        if normalized_key in self.color_map:
            return self.color_map[normalized_key]
        hash_value = hashlib.md5(normalized_key.encode()).hexdigest()[:6]
        base_hex = "#0000" + hash_value.upper()
        return f"{base_hex}"
    def _normalize_input(self, input_str: str) -> str:
        cleaned = "".join(c for c in input_str if c.isalnum())
        return self._standardize_region(cleaned)
    def _standardize_region(self, region: str) -> str:
        standard_map = {
            "downtown": "downtown",
            "city center": "downtown",
            "urban core": "downtown"
        }
        if region in standard_map:
            return standard_map[region]
        parts = region.split()
        if len(parts) == 2 and parts[1].startswith("sub"):
            return "suburbs"
        if any(word.startswith("ind") for word in parts):
            return "industrial"
        if all(word.endswith("al") or word.startswith("residential") for word in parts[:3]):
            return "residential"
        key = f"{parts[0]}{parts[1]}" if len(parts) >= 2 else region
        h = hashlib.md5(key.encode()).hexdigest()[:6]
        colors = ["#FFD733", "#8B4513"]                                                           
        return f"#{h}"
if __name__ == '__main__':
    mapper = AreaColorMapper()
    test_cases = [
        "downtown district",
        "city center area",
        "suburban zone 123",
        "industrial park north",
        "residential neighborhood west"
    ]
    results = []
    for case in test_cases:
        color = mapper.generate_color(case)
        results.append(f"{case} -> {color}")
    print("\n".join(results))