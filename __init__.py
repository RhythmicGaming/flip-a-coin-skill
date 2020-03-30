from mycroft import MycroftSkill, intent_file_handler


class FlipACoin(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('coin.a.flip.intent')
    def handle_coin_a_flip(self, message):
        self.speak_dialog('coin.a.flip')


def create_skill():
    return FlipACoin()

