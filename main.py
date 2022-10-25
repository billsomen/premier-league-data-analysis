from dotenv import load_dotenv
from models.premier_league import PremierLeague
from utils.main_lib import argparser

# load environment variable from .env file
load_dotenv()


def run() -> None:
    """
    Run the script
    """

    # Grab command line args
    args = argparser()

    # Create an object of Premier League class for seasons 2020, 2021 and 2022
    premier_league = PremierLeague(args.season_list)

    # Write CSV files for all seasons in the format season-{year}.csv
    premier_league.export_season_list_to_csvs(args.output_dir)


if __name__ == "__main__":
    run()
