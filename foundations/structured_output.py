import os

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]



completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed
event.name
event.date
event.participants

#EXPLANATION
#Pydantic is used to structure the output that the llm gives like if we need an output in a certain format we can define a custom model using the basemodel from pydantic
#Here the structure defined includes the name and its data type and similarly each variable is mentioned too.
# the response format too is included in the api call to open ai server ,so it returns the output in that format