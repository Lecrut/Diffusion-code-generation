import pandas as pd
import numpy as np
import logging
from datetime import datetime
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache_dir = Path("cache")
        self.cache_dir.mkdir(exist_ok=True)
    def validate_input(self, data_frame):
        if not isinstance(data_frame, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        required_columns = ['id', 'value']
        missing_cols = [col for col in required_columns if col not in data_frame.columns]
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            raise ValueError(f"DataFrame must contain columns: {required_columns}.")
        nan_count = data_frame.isna().sum()
        if any(nan_count > 0):
            logger.warning(f"Found missing values in column(s): {nan_count[nan_count > 0].index.tolist()}")
    def load_from_cache(self, filename: str) -> pd.DataFrame:
        file_path = self.cache_dir / f"{filename}.pkl"
        logger.info(f"Checking for cached file: {file_path}")
        try:
            import pickle
            with open(file_path, 'rb') as handle:
                df = pickle.load(handle)
            logger.info("Data loaded from cache successfully.")
            return df
        except FileNotFoundError:
            logger.warning(f"Cache miss for {filename}. Loading fresh data.")
            return None
    def save_to_cache(self, filename: str):
        file_path = self.cache_dir / f"{filename}.pkl"
        import pickle
        try:
            with open(file_path, 'wb') as handle:
                pickle.dump(self.current_data_frame, handle)
            logger.info(f"Data saved to cache at {file_path}")
        except Exception as e:
            logger.error(f"Failed to save data to cache: {e}")
    def process_data(self):
        raw_data = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'value': [10.5, np.nan, 20.0, 30.0]
        })
        logger.info("Starting data processing pipeline.")
        self.validate_input(raw_data)
        cached_df = self.load_from_cache('raw')
        if cached_df is not None and len(cached_df) > 0:
            logger.info("Using previously processed data.")
            df_to_process = raw_data.copy()
        else:
            cleanable_cols = ['value']
            imputed_values = {}
            for col in cleanable_cols:
                if np.isnan(raw_data[col].mean()):
                    logger.warning(f"Cannot compute mean for {col}, filling with 0.")
                    fill_val = 0.0
                else:
                    fill_val = raw_data[col].mean()
                imputed_values[col] = fill_val
            cleaned_df = raw_data.fillna(imputed_values)
            logger.info("Data cleaning completed with NaN replacement.")
        self.current_data_frame = cleaned_df
        self.save_to_cache('cleaned')
        logger.info("Performing statistical transformations.")
        transformed_data = cleaned_df.copy()
        mean_val = transformed_data['value'].mean()
        std_val = transformed_data['value'].std()
        if pd.isna(std_val):
            std_val = 1.0
        normalized_values = (transformed_data['value'] - mean_val) / std_val
        transformed_data['normalized_value'] = normalized_values
        logger.info(f"Transformation complete. Mean: {mean_val:.2f}, Std: {std_val:.2f}")
    def export_results(self, filename='output'):
        file_path = Path("results") / f"{filename}.csv"
        try:
            with open(file_path, 'w') as handle:
                self.current_data_frame.to_csv(handle)
            logger.info(f"Results exported to {file_path}")
        except Exception as e:
            logger.error(f"Failed to export results: {e}")
if __name__ == '__main__':
    pipeline = DataPipeline()
    try:
        pipeline.process_data()
        pipeline.export_results('final_analysis')
        logger.info("Data analysis pipeline executed successfully.")
    except Exception as e:
        logger.critical(f"Pipeline execution failed with error: {e}")