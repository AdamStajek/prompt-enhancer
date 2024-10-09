from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.get_api_key())


class PromptManager:
    def __init__(self, model="gpt-4o"):
        self.model = model

    def prompt_gpt(self, prompt: str) -> str:
        """
        A function which prompts appropriate gpt model.

        :param prompt: a prompt to OpenAI api
        :return: gpt's answer
        """
        completion = client.chat.completions.create(
              model=self.model,
              messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
              ]
        )
        return completion.choices[0].message.content
