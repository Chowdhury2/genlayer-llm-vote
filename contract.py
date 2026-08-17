# Simple LLM Decision Contract Logic
class LLMVoteContract:
    def __init__(self):
        self.votes_yes = 0
        self.votes_no = 0

    def process_vote(self, input_text):
        if "yes" in input_text.lower():
            self.votes_yes += 1
            return "Voted Yes"
        else:
            self.votes_no += 1
            return "Voted No"
