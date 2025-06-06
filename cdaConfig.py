import configLoader
import os


class CdaConfig(configLoader.StrictBaseModel):
    token_user: str
    token: str
    credentials: str = os.path.join(os.environ["HOME"], ".config/gspread/credentials.json")


def main() -> None:
    configLoader.load("cda-config.yaml", CdaConfig)


if __name__ == "__main__":
    main()
