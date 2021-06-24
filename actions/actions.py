# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ValidaNomeForm(FormValidationAction):
    """Verifica o nome do usuário"""

    ##### Nome do form para o Rasa
    def name(self) -> Text:
        """Identifica o form na estória do Rasa."""
        return "validate_nome_form"

    ##### Validação do nome
    def validate_nome(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(slot_value)

        nome = slot_value

        if nome == 'Rafael':
            dispatcher.utter_message(text = nome)
        elif nome == 'Michael':
            dispatcher.utter_message(text = nome)
        else:
            dispatcher.utter_message(text = nome)