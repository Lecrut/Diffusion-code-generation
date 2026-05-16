class VolumeConverter:
    @staticmethod
    def metric_to_imperial_liters(volume_liters: float) -> float:
        return volume_liters * 0.264172
    @staticmethod
    def metric_to_imperial_gallons(volume_liters: float) -> float:
        return volume_liters * 0.264172
    @staticmethod
    def imperial_to_metric_liters(volume_gallons: float) -> float:
        return volume_gallons / 0.264172
    @staticmethod
    def imperial_to_metric_gallons(volume_gallons: float) -> float:
        return volume_gallons
if __name__ == '__main__':
    sample_metric_volume_l = 10.0
    sample_imperial_volume_gal = 3.0
    print(f"--- Metric to Imperial Conversion ---")
    print(f"{sample_metric_volume_l} Liters is equal to {VolumeConverter.metric_to_imperial_gallons(sample_metric_volume_l):.4f} Gallons")
    print(f"\n--- Imperial to Metric Conversion ---")
    print(f"{sample_imperial_volume_gal} Gallons is equal to {VolumeConverter.imperial_to_metric_liters(sample_imperial_volume_gal):.4f} Liters")
    sample_metric_volume_ml = 500.0
    print(f"\n--- Metric to Imperial (mL Example) ---")
    print(f"{sample_metric_volume_ml} mL is equal to {VolumeConverter.metric_to_imperial_gallons(sample_metric_volume_ml / 1000.0):.4f} Gallons")