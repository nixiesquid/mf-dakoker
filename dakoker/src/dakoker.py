# coding:utf-8
import fire
from src.account_manager import AccountManager


class Dakoker(object):

    def __init__(self):
        self.manager = AccountManager()

    def start(self):
        if self.manager.login():
            self.manager.clock_in()
            self.manager.exit()

    def stop(self):
        if self.manager.login():
            self.manager.clock_out()
            self.manager.exit()


def main():
    fire.Fire(Dakoker)