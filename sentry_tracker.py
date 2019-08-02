import sentry_sdk

sentry_sdk.init(
    "https://9073cd843bbe4513852ab2ecce615e1b@sentry.io/1519850", release="test@0.0.0"
)
# test pwd
division_by_zero = 8 / 0
