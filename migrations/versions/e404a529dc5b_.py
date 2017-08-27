"""empty message

Revision ID: e404a529dc5b
Revises: 7871961f26f2
Create Date: 2016-07-21 01:13:01.377403

"""

# revision identifiers, used by Alembic.
revision = 'e404a529dc5b'
down_revision = '7871961f26f2'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(), nullable=True),
    sa.Column('mail_status', sa.Integer(), nullable=True),
    sa.Column('notif_status', sa.Integer(), nullable=True),
    sa.Column('user_control_status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message_settings')
    ### end Alembic commands ###