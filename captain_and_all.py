from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/captain_and_all.db")
    #app.run()
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)
    session.commit()

    session = db_session.create_session()
    user = User()
    user.surname = "Elisabeth"
    user.name = "Swan"
    user.age = 17
    user.position = "pirat"
    user.speciality = "dutchess"
    user.address = "module_12"
    user.email = "swan1234@mars.org"
    user.hashed_password = "miss"
    session.add(user)
    session.commit()

    session = db_session.create_session()
    user = User()
    user.surname = "Jeck"
    user.name = "Sparrow"
    user.age = 36
    user.position = "captainJeck"
    user.speciality = "captain_2"
    user.address = "module_3"
    user.email = "bestcaptain@mars.org"
    user.hashed_password = "BESTCAP"
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()