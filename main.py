import sentry_sdk

sentry_sdk.init(
    dsn="https://c493db87c62f55a0cac221440e72f924@o4509984167755776.ingest.us.sentry.io/4509984312983552",
    send_default_pii=True,
)


if __name__ == "__main__":
    division_by_zero = 1 / 0