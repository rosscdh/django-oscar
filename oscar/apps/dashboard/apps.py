try:
    from django.apps import AppConfig

    class PromotionsConfig(AppConfig):
        label = 'oscar.apps.dashboard.promotions'
        name = 'dashboard.promotions'  # this is the new unique name for this app in 1.7

except:
    # not using 1.7
    pass