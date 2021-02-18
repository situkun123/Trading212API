from pytrading212.order import TimeValidity, StopLimitOrder, StopOrder, LimitOrder

from pytrading212 import Trading212, Mode, MarketOrder
from pytrading212.trading212 import Period

trading212 = Trading212('your_email', 'password', mode=Mode.DEMO)

market_order = trading212.execute_order(MarketOrder(instrument_code="AMZN_US_EQ", quantity=2))

limit_order = trading212.execute_order(
    LimitOrder(instrument_code="AMZN_US_EQ", quantity=2, limit_price=3000, time_validity=TimeValidity.DAY))

stop_order = trading212.execute_order(
    StopOrder(instrument_code="AMZN_US_EQ", quantity=2, stop_price=4000, time_validity=TimeValidity.GOOD_TILL_CANCEL))

stop_limit = trading212.execute_order(
    StopLimitOrder(instrument_code="AMZN_US_EQ", quantity=2, limit_price=3000, stop_price=4000,
                   time_validity=TimeValidity.GOOD_TILL_CANCEL))

funds = trading212.get_funds()
orders = trading212.get_orders()

portfolio = trading212.get_portfolio_composition()
performance = trading212.get_portfolio_performance(Period.LAST_DAY)

trading212.finish()