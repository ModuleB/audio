from app.dao.user_dao import UserDAO
from app.database import db_session
from app.services.user_service import UserService


user_dao = UserDAO(db_session)
user_service = UserService(user_dao)
# record_dao = RecordDAO()
# record_service = RecordService(record_dao)
